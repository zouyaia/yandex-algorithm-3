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
const int N = (int)1e3 + 2;
const ll BIG = 1e18;
const db PI = acos((db)-1);

vector< vector<int> > g(N, vector<int>());

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
//    freopen("input.txt", "r", stdin);
    int n, m;
    cin >> n >> m;
    for(int j = 0; j < m; j++) {
        int fr, to;
        cin >> fr >> to;
        g[to].push_back(fr);
    }
    int s = 1;
    queue<int> q;
    q.push (s);
    vector<bool> used (n);
    used[s] = true;
    vector<int> ans;
    ans.push_back(s);
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        for (int i=0; i<g[v].size(); ++i) {
            int to = g[v][i];
            if (!used[to]) {
                ans.push_back(to);
                used[to] = true;
                q.push(to);
            }
        }
    }
    sort(ans.begin(), ans.end());
    for(int i = 0; i < ans.size(); i++)
        cout << ans[i] << ' ';
    return 0;
}