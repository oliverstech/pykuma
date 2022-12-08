from distutils.core import setup
setup(
  name = 'pykuma',        
  packages = ['pykuma'],   
  version = '1.0.2',      
  readme = "README.md",
  license='MIT',        
  description = 'An API for Python and Uptime Kuma integration',   
  author = 'oliverstech',                   
  author_email = 'mail@oliverstech.tk',      
  url = 'https://github.com/oliverstech/pykuma',   
  keywords = ['uptime', 'api', 'pykuma', 'kuma'],   
  install_requires=[           
          'requests',
          'asyncio',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
