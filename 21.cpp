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
const int N = (int)1e6;
const ll BIG = 1e18;
const db PI = acos((db)-1);

vector<int> cbs;
int dp[N+1];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
//    freopen("input.txt", "r", stdin);

    int n;
    cin >> n;

    dp[0] = 0;
    fill(dp, dp+N+1, N+1);

    for(int i = 1; i <= (int)1e2; i++){
        int t = (int)pow(i, 3);
        cbs.pb(t);
        dp[t] = 1;
    }

    for(int i = 0; i < n; i++) {
        for(auto c: cbs) {
            if(i + c <= N) {
                if (dp[i] != N + 1)
                    dp[i + c] = min(dp[i + c], dp[i] + 1);
            } else
                break;
        }
    }

    cout << dp[n] << endl;

    return 0;
}