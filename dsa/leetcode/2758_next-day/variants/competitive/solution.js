/**
 * @return {string}
 */
Date.prototype.nextDay = function() {
    const next = new Date(this);
    next.setUTCDate(next.getUTCDate() + 1);
    return next.toISOString().slice(0, 10);
};

/**
 * const date = new Date("2014-06-20");
 * date.nextDay(); // "2014-06-21"
 */
