#include <stdint.h>
#include <stdlib.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

EXPORT int nth_xor_prime_c(int target, int bit_limit) {
    if (target == 1) return 2;
    int limit = 1 << bit_limit;
    int half_limit = limit >> 1;

    uint8_t *mark = (uint8_t*)calloc(half_limit, 1);
    if (!mark) return -1;
    mark[0] = 1;

    int found = 1;
    int result = 0;

    for (int base = 3; base < limit; base += 2) {
        if (mark[base >> 1]) continue;

        found++;
        if (found == target) {
            result = base;
            break;
        }

        int degree = 31 - __builtin_clz(base);
        int max_cofactor_degree = bit_limit - degree - 1;

        for (int cofactor_degree = degree; cofactor_degree <= max_cofactor_degree; cofactor_degree++) {
            uint32_t product = (base << cofactor_degree) ^ base;
            mark[product >> 1] = 1;

            int variants = 1 << (cofactor_degree - 1);
            for (int n = 1; n < variants; n++) {
                int toggled_bit = __builtin_ctz(n) + 1;
                product ^= (base << toggled_bit);
                mark[product >> 1] = 1;
            }
        }
    }

    free(mark);
    return result;
}
