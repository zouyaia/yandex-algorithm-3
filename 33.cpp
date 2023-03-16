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
const int N = 1201;
const ll BIG = 1e18;
const db PI = acos((db)-1);

int n, mid;
vector< pair<int, int> > cd;
int r[N][N];
int col[N];
bool flag;

void dfs(int v) {
    for(int u = 0; u < n; u++) {
        if(u==v or r[v][u]>=mid)
            continue;
        if(col[u] == 0) {
            col[u] = 3-col[v];
            dfs(u);
        } else if(col[u]==col[v]) {
            flag = flag && false;
        }
    }
}

bool solve() {
    fill(col, col+n, 0);
    flag = true;
    for(int i = 0; i < n; i++) {
        if(col[i]==0) {
            col[i] = 1;
            dfs(i);
        }
    }
    return flag;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    freopen("input.txt", "r", stdin);

    cin >> n;
    for(int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;
        cd.push_back(mp(x, y));
    }

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            pair<int, int> p1=cd[i], p2=cd[j]; // 8^10**8 - max r,
            r[i][j] = pow(p1.first-p2.first, 2)+pow(p1.second-p2.second, 2);
        }
    }

    int left=0, right=MOD;
    while (left + 1 < right) {
        mid = (left+right) / 2;
        if (solve()) {
            left = mid;
        } else {
            right = mid-1;
        }
    }
    mid = right;
    bool bl=solve();
    if(!bl) {
        mid = left;
        bl = solve();
    }
    cout.precision(12);
    cout << sqrt((double)mid/4) << '\n';
    for(int i = 0; i < n; i++) {
        if(col[i]==0)
            cout << 1 << ' ';
        else
            cout << col[i] << ' ';
    }
    return 0;
}