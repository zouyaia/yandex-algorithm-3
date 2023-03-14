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
const int N = 11;
const ll BIG = 1e18;
const db PI = acos((db)-1);

int g[N][N]; // граф
int n; // число вершин

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
//    freopen("input.txt", "r", stdin);
    cin >> n;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            char c;
            cin >> c;
            if(c=='*')
                g[i][j] = 0;
            else
                g[i][j] = 1;
        }
    }
    int si, sj;
    cin >> si >> sj;
    queue< pair<int, int> > q;
    q.push(mp(si-1, sj-1));
    vector< vector<bool> > used (n, vector<bool> (n, false));
    used[si-1][sj-1] = true;
    int ans = 1;
    pair<int, int> moves[4] = {mp(1, 0), mp(0, 1), mp(0, -1), mp(-1, 0)};
    while (!q.empty()) {
        pair<int, int> v = q.front();
        q.pop();
        for (auto move: moves) {
            pair<int, int> to = mp(v.first + move.first, v.second + move.second);
            if (!used[to.first][to.second] && g[to.first][to.second]) {
                used[to.first][to.second] = true;
                q.push (to);
                ans++;
            }
        }
    }
    cout << ans;
    return 0;
}