from ipykernel.kernelapp import IPKernelApp
from .kernel import MyPythonKernel
IPKernelApp.launch_instance(kernel_class=MyPythonKernel)
