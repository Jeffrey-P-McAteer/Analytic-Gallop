
import os
import sys
import subprocess
import shutil

def title(title_str):
  print('=' * 12, title_str, '=' * 12)

def main(args=sys.argv):
  os.chdir(os.path.dirname(__file__))

  title('Building')
  subprocess.run([
    'cargo', 'build', '--release',
  ], cwd='analytic-gallop')
  shutil.copy(
    os.path.join(
      'analytic-gallop', 'target', 'release', 'libanalytic_gallop.so'
    ),
    os.path.join(
      'analytic-gallop', 'target', 'release', 'analytic_gallop.pyd'
    )
  )


  title('Test')
  os.environ['PYTHONPATH'] = os.pathsep.join([
    os.environ.get('PYTHONPATH', ''),
    os.path.abspath(os.path.join(
      'analytic-gallop',
      'target',
      'release',
    ))
  ])
  subprocess.run([
    'python', 'tests/discover_coastlines.py'
  ], env=os.environ)



if __name__ == '__main__':
  main()

