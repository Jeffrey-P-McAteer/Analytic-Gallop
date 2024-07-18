
import os
import sys
import subprocess
import shutil

def title(title_str):
  print('=' * 12, title_str, '=' * 12)

def copy_ife(source_path, dest_path):
  sp = os.path.join(*source_path)
  if os.path.exists(sp):
    shutil.copy(sp, os.path.join(*dest_path))

def main(args=sys.argv):
  os.chdir(os.path.dirname(__file__))

  title('Building')
  subprocess.run([
    'cargo', 'build', '--release',
  ], cwd='analytic-gallop', check=True)
  copy_ife(
    [ 'analytic-gallop', 'target', 'release', 'libanalytic_gallop.so' ],
    [ 'analytic-gallop', 'target', 'release', 'analytic_gallop.pyd' ]
  )
  copy_ife(
    [ 'analytic-gallop', 'target', 'release', 'analytic_gallop.dll' ],
    [ 'analytic-gallop', 'target', 'release', 'analytic_gallop.pyd' ]
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
  ], env=os.environ, check=True)



if __name__ == '__main__':
  main()

