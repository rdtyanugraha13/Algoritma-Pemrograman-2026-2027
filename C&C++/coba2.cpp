#include <iostream>
#include <string>
using namespace std;

int main() {
    int umur = 19;
    double tinggi = 170.5;
    char kelas = 'A';
    bool aktif = true;
    string nama = "Mochamad Raditya Nugraha";

    const string KAMPUS = "Universitas Djuanda";

    cout << "int  umur = " << umur << endl;
    cout << "double tinggi = " << tinggi << endl;
    cout << "char  kelas = " << kelas << endl;
    cout << "bool  aktif = " << aktif << endl;
    cout << "string nama = " << nama << endl;
    cout << "const = " << KAMPUS << endl;
    return 0;
}