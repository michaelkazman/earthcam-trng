#include <stdio.h>
#include <Python.h>
//#include <python3.8/Python.h>
//#include <python3.8/cpython/initconfig.h>
int main() {

   Py_Initialize();

   /* This is to add the path in the code */
   PyObject *sys = PyImport_ImportModule("sys");
   PyObject *path = PyObject_GetAttrString(sys, "path");
   PyList_Append(path, PyUnicode_FromString("."));

    /* 1st: Import the file with the name as param*/
   PyObject* ModuleString = PyUnicode_FromString("rand");
   if (!ModuleString) {
        PyErr_Print();
        printf("Error formating python script\n");
    }
    PyObject* Module = PyImport_Import(ModuleString);
    if (!Module) {
        PyErr_Print();
        printf("Error importing python script\n");
    }

   /* 2nd: Getting reference to the function with the function name as param*/
    PyObject* Function = PyObject_GetAttrString(Module,"get_num");
    if (!Function) {
        PyErr_Print();
        printf("Pass valid argument to get_num()\n");
    }

   //call function
    PyObject* result = PyObject_CallObject(Function, NULL);
   //conert python object into c object
   unsigned char *bytes = (unsigned char *)PyBytes_AS_STRING(result);
   
   printf("python rand bytes is %s\n", bytes);
   

   Py_Finalize();

   return 0;
}