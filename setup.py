from setuptools import setup
import os
setup(name='jupyter_MyPython_kernel',
      version='0.0.1',
      description='Minimalistic Python kernel for Jupyter',
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/nufeng1999/jupyter-MyPython-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyPython-kernel/tarball/0.0.1',
      packages=['jupyter_MyPython_kernel'],
      scripts=['jupyter_MyPython_kernel/install_MyPython_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'python','py'],
      include_package_data=True
      )
