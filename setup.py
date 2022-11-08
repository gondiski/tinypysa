import setuptools

setup(
        name='tinypesa',
        version='0.1.0',
        description='An Mpesa STK push payments solution',
        url='https://github.com/gondiski/tinypysa',
        author='Enoch Otieno',
        author_email='enochotieno@rocketmail.com',
        license='BSD 2-clause',
        packages=['tinypesa'],
        install_requires=['requests'],
        classifiers=[
            'Development Status :: 1 - Development',
            'Intended Audience :: E-commerce/Payments',
            'License :: OSI Approved :: BSD License',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 3'
            ],
        )
