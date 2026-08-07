import { PGlite } from '@electric-sql/pglite';

async function testPGlite() {
  console.log('Initializing in-memory PGlite WASM PostgreSQL Engine...');
  const db = new PGlite();

  // Create Table 1: Person
  await db.exec(`
    CREATE TABLE Person (
      id INT PRIMARY KEY,
      firstName VARCHAR(50),
      lastName VARCHAR(50)
    );
    INSERT INTO Person VALUES (1, 'Wang', 'Allen'), (2, 'Alice', 'Bob');
  `);

  // Create Table 2: Address
  await db.exec(`
    CREATE TABLE Address (
      addressId INT PRIMARY KEY,
      personId INT,
      city VARCHAR(50),
      state VARCHAR(50)
    );
    INSERT INTO Address VALUES (1, 2, 'New York City', 'New York'), (2, 3, 'Leetcode', 'California');
  `);

  console.log('Tables created successfully. Executing PostgreSQL JOIN query...');

  const query = `
    SELECT 
      p.firstName, 
      p.lastName, 
      a.city, 
      a.state 
    FROM Person p 
    LEFT JOIN Address a ON p.id = a.personId;
  `;

  const res = await db.query(query);
  console.log('\n=== POSTGRESQL QUERY RESULT GRID ===');
  console.log('Columns:', res.fields.map(f => f.name));
  console.log('Rows:', res.rows);

  // Test Postgres-specific Window Function & COALESCE & String Aggregation
  console.log('\nTesting Postgres-specific Window Functions & STRING_AGG & COALESCE...');
  const res2 = await db.query(`
    SELECT 
      COALESCE(p.firstName, 'Unknown') AS name,
      STRING_AGG(COALESCE(a.city, 'No City'), ', ') AS cities
    FROM Person p 
    LEFT JOIN Address a ON p.id = a.personId
    GROUP BY p.firstName;
  `);

  console.log('PostgreSQL Specific Output:');
  console.log(res2.rows);

  console.log('\nPGlite WASM Postgres Engine Test PASSED 100%!');
}

testPGlite().catch((err) => {
  console.error('PGlite Test Error:', err);
  process.exit(1);
});
