# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

setup(
    name="speechmetrics",
    version="1.0",
    packages=find_packages(),

    install_requires=[
        'numpy',
        'scipy',
        'tqdm',
        'resampy',
        'pystoi',
        'museval',
        # This is requred, but srmrpy pull it in,
	    # and there is a pip3 conflict if we have the following
	    # line.
        #'gammatone @ git+https://ghproxy.com/https://github.com/detly/gammatone',
        'pypesq @ git+https://ghproxy.com/https://github.com/vBaiCai/python-pesq',
        # 'srmrpy @ git+https://ghproxy.com/https://github.com/jfsantos/SRMRpy',
	'srmrpy @ git+https://ghproxy.com/https://github.com/yanplr/SRMRpy',
#         'pesq @ git+https://ghproxy.com/https://github.com/ludlows/PESQ',
	'pesq @ git+https://ghproxy.com/https://github.com/A-d-DASARE/python-pesq',
	    
    ],
    extras_require={
        'cpu': ['tensorflow>=2.0.0', 'librosa'],
        'gpu': ['tensorflow-gpu>=2.0.0', 'librosa'],
    },
    include_package_data=True
)
