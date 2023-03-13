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
const int N = (int)2e5 + 5;
const ll BIG = 1e18;
const db PI = acos((db)-1);

map<char, int> m;
vector<string> v;
int d[6][101];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    freopen("input.txt", "r", stdin);
    string s1="NSWEUD";
    for(int i=0; i<s1.size(); i++)
        m[s1[i]] = i;
    char c2[101];
    for(int i=0; i<6; i++) {
        cin.getline(c2, 101, '\n');
        string s2(c2);
        v.pb(s2);
    }
    char c;
    int x;
    cin >> c >> x;

    for(int i = 0; i < 6; i++)
        for(int j = 0; j < 101; j++)
            d[i][j] = 0;
    for(int i = 0; i < 6; i++)
        d[i][0] = 1;
    for(int i = 0; i < 6; i++)
        d[i][1] = 1+v[i].size();
    for(int j = 2; j < x; j++) {
        for(int i = 0; i < 6; i++) {
            d[i][j] += 1;
            for(auto u: v[i]) {
                d[i][j] += d[m[u]][j-1];
            }
        }
    }

    cout << d[m[c]][x-1];
    return 0;
}