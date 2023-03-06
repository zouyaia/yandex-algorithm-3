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

using ll = long long;
using db = long double; // or double, if TL is tight
using str = string;

// pairs
using pi = pair<int, int>;
using pl = pair<ll, ll>;
using pd = pair<db, db>;
#define mp make_pair
#define f first
#define s second

#ifdef ONPC
mt19937 rnd(228);
#else
mt19937 rnd(chrono::high_resolution_clock::now().time_since_epoch().count());
#endif

// vectors
#define ins insert
#define pb push_back
#define eb emplace_back

#define lb lower_bound
#define ub upper_bound

const int MOD = (int)1e9 + 7; // 998244353;
const int N = (int)2e5 + 5;
const ll BIG = 1e18; // not too close to LLONG_MAX
const db PI = acos((db)-1);

int main() {
// #ifdef ONPC
//     freopen("a.in", "r", stdin);
// #endif
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    deque<int> q;
    queue<pi> q2;

    while (t--) {
        char c;
        int i, pr=0;
        cin >> c;
        if(c=='+'){
            cin >> i;
            q.pb(i);
        }else if(c=='*'){
            cin >> i;
            int mid = (int)(q.size()+1)/2;
            cout << q[mid] << "\n";
            q2.push(make_pair(i, q[mid]));
        }else if(c=='-'){
            pi p = q2.front();
            if (pr == p.s){
                cout << p.f << "\n";
            }


            cout << q.front() << "\n";
            q.pop();
        }
    }

    return 0;
}