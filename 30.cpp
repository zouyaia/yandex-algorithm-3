#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <chrono>
#include <climits>
#include <cmath>
#include <complex>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <random>
#include <set>
#include <vector>
using namespace std;

typedef long long ll;
typedef long double db;
typedef pair<int, int> pi;
typedef pair<ll, ll> pl;
#define mp make_pair
#define ins insert
#define pb push_back
#define eb emplace_back
#define lb lower_bound
#define ub upper_bound

const int MOD = (int)1e9 + 7;
const int N = 105;
const ll BIG = 1e18;
const db PI = acos((db)-1);

int len, n;
int c[N];
int dp[N][N];

int solve(int l, int r) {
    if(r-l <= 1)
        return 0;
    if(dp[l][r] != MOD)
        return dp[l][r];
    for(int i = l+1; i < r; i++) {
        dp[l][i] = solve(l, i);
        dp[i][r] = solve(i, r);
        dp[l][r] = min(dp[l][r], dp[l][i]+dp[i][r]+c[r]-c[l]);
    }
    return dp[l][r];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
//    freopen("input.txt", "r", stdin);

    cin >> len >> n;
    c[0] = 0;
    for(int i = 1; i <= n; i++)
        cin >> c[i];
    c[n+1] = len;
    n = n+2;
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
            dp[i][j] = MOD;
    int ans = solve(0, n-1);
    cout << ans;
    return 0;
}