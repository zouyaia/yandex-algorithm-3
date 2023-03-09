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
const int N = (int)1e3+1;
const ll BIG = 1e18;
const db PI = acos((db)-1);

int a[N];
int dp[N];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    freopen("input.txt", "r", stdin);

    int n;
    cin >> n;

    for(int i = 0; i < n; i++)
        cin >> a[i];

    fill(dp, dp+N, 1);
    for(int i = 0; i < n; i++) {
        for(int j = i; j < n; j++) {
            if (a[j] > a[i])
                dp[j] = max(dp[j], dp[i] + 1);
        }
    }

    int mx=1, mix=0;
    for(int i = 0; i < n; i++){
        if(dp[i] > mx) {
            mx = dp[i];
            mix = i;
        }
    }
    vector<int> ans;
    ans.pb(a[mix]);
    int i = mix;
    while(dp[i] != 1) {
        int j;
        for(j = i; j >= 0; --j) {
            if (dp[j]+1 == dp[i] && a[j] < a[i])
                break;
        }
        ans.pb(a[j]);
        i = j;
    }

    reverse(ans.begin(), ans.end());
    for (auto u: ans)
        cout << u << ' ';

    return 0;
}
