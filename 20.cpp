#include <array>
#include <cmath>
#include <iostream>
#include <set>
using namespace std;

using ll = long long;
using db = long double; // or double, if TL is tight

// pairs
using pi = pair<int, int>;
#define mp make_pair
#define s second

// vectors
#define ins insert
#define pb push_back
#define eb emplace_back

#define lb lower_bound
#define ub upper_bound

const int N = (int)1e5 + 1;
const int P = (int)5e5 + 1;

int x[P], ix[P], lu[N];
multiset<pi> m;

int main() {
    int n, k, p;
    cin >> n >> k >> p;
    for(int i = 0; i < n; i++)
        lu[i] = p;

    for(int i = 0; i < p; i++) {
        cin >> x[i];
        x[i]--;
        ix[i] = p;
    }

    for(int i = p-1; i >= 0; i--) {
        ix[i] = lu[x[i]];
        lu[x[i]] = i;
    }
    bool f[n];
    fill(f, f+n, false);
    int ans = 0;
    for(int i = 0; i < p; i++) {
        if ((int)m.size() < k && !f[x[i]]) {
            if (ix[i] != p)
                m.insert(mp(-ix[i], x[i]));
            f[x[i]] = true;
            ans++;
        } else if (!f[x[i]]) {
            pi pr = (*m.begin());
            m.erase(m.begin());
            if (ix[i] != p)
                m.insert(mp(-ix[i], x[i]));
            f[x[i]] = true;
            f[pr.s] = false;
            ans++;
        } else {
            pi pr = mp(-i, x[i]);
            m.erase(m.lb(pr));
            if (ix[i] != p)
                m.insert(mp(-ix[i], x[i]));
        }
    }
    cout << ans;

    return 0;
}