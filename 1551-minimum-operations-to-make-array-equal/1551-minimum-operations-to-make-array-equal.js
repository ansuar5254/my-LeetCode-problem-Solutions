/**
 * @param {number} n
 * @return {number}
 */
var minOperations = function(n) {
    let m = Math.floor(n / 2);
    let ans = 0;
    
    if (n % 2 !== 0) {
        let i = 2;
        while (m) {
            ans += i;
            i += 2;
            m -= 1;
        }
    } else {
        let i = 1;
        while (m) {
            ans += i;
            i += 2;
            m -= 1;
        }
    }
    return ans;
};