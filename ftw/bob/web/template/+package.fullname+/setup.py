from setuptools import setup, find_packages


extras_require = {
    'tests': [
        'plone.app.testing',
        'unittest2',
    ],
}

setup(name='{{{package.fullname}}}',
      version='1.0.0.dev0',
      author='4teamwork AG',
      url='https://github.com/4teamwork/{{{package.fullname}}}',
      license='GPL2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['{{{package.part_1}}}'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
          'errbit',
          'ftw.footer',
          'ftw.inflator[dexterity]',
          'ftw.lawgiver',
          'ftw.mobilenavigation',
          'ftw.upgrade',
          'Plone',
          'plonetheme.onegovbear',
          'setuptools',
      ],

      tests_require=extras_require['tests'],
      extras_require=extras_require,

      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
