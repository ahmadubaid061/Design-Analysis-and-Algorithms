#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <iomanip>

using namespace std;

// Returns operation count and writes elapsed time (ms) into elapsed_time_ms
long long exchange_sort_with_metrics(vector<int>& arr, double& elapsed_time_ms) {
    long long operation_count = 0;

    auto start_tick = chrono::steady_clock::now();

    int n = arr.size();
    operation_count += 1;

    for (int i = 0; i < n; i++) {
        operation_count += 2;

        operation_count += 1;
        for (int j = i + 1; j < n; j++) {
            operation_count += 2;

            operation_count += 1;
            if (arr[i] > arr[j]) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                operation_count += 3;
            }
        }
    }

    auto end_tick = chrono::steady_clock::now();
    elapsed_time_ms = chrono::duration<double, milli>(end_tick - start_tick).count();

    return operation_count;
}

void print_array(const vector<int>& arr) {
    cout << "[";
    for (size_t i = 0; i < arr.size(); i++) {
        cout << arr[i];
        if (i + 1 < arr.size()) cout << " ";
    }
    cout << "]";
}

int main() {
    // Equivalent of np.random.randint(0, 1001, size=1000)
    mt19937 gen(random_device{}());
    uniform_int_distribution<int> dist(0, 1000);

    vector<int> array(1000);
    for (int& x : array) {
        x = dist(gen);
    }

    cout << "Original List: ";
    print_array(array);
    cout << "\n\n";

    double duration = 0.0;
    long long total_ops = exchange_sort_with_metrics(array, duration);

    cout << "Sorted List:   ";
    print_array(array);
    cout << "\n";
    cout << "Total Operations Tracked: " << total_ops << "\n";
    cout << "Elapsed Time: " << fixed << setprecision(4) << duration << " ms\n";

    return 0;
}