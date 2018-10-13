#include <Python.h>
#include "BubbleSort.h"

//static PyObject *mod_met(PyObject *self){
//static PyObject *mod_met(PyObject *self, PyObject *args, PyObject *kw){
static PyObject *mod_met(PyObject *self, PyObject *args){
	int a=0,b=0;
	int c =0;
	//PyObject *c;
	if(!PyArg_ParseTuple(args, "i|ii", &a, &b, &c)){ //jezeli do stringa wstawi sie | to po sa opcjonalne
		//docs.python.org/3.4/c-api/arg.html
		//docs.python.org/3.4/c-api/concrete.html
		//docs.python.org/3.4/c-api/object.html
		//docs.python.org/3.4/c-api/exceptions.html
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
	//Py_RETURN_NONE; //jesli nic nie zwraca
	return Py_BuildValue("i", a+b+c);
}

static PyObject *mod_bubble(PyObject *self, PyObject *args){
	PyObject *mylist;
	
	if(!PyArg_ParseTuple(args, "O", &mylist)){ 
		return NULL;
	}
	
	long si = PyList_Size(mylist);
	long t[si];

	for(long i=0;i<si;i++){
		t[i]=PyLong_AsLong(PyList_GetItem(mylist,i));
	}

	bubb(si,t);

	for(long i=0;i<si;i++){
		PyList_SetItem(mylist,i,PyLong_FromLong(t[i]));
	}	

	return Py_BuildValue("O", mylist);
}

//tablica metod
static PyMethodDef mod_metody[]={
	{"met", (PyCFunction)mod_met, METH_VARARGS, "Funkcja ..."},
	{"bubble", (PyCFunction)mod_bubble, METH_VARARGS, "BubbleSort..."}, 
	//nazwa funkcja stosowana w Pythonie, adres funkcji , j.w. lub METH_KEYWORDS lub METH_NOARGS, lancuch dokumentacyjny
	{NULL, NULL, 0, NULL}	//wartownik
};


static struct PyModuleDef modmodule={
        PyModuleDef_HEAD_INIT,
        "mod",
        NULL,
        -1,
        mod_metody
};

//funkcja inicjalizujaca
PyMODINIT_FUNC PyInit_mod(void){
        return PyModule_Create(&modmodule);
}
