"""Package only the browser runtime for static hosting."""
from pathlib import Path
import shutil
root = Path(__file__).resolve().parent.parent
output = root / 'dist'
files = ['index.html', 'blackbox-app.js', 'blackbox-base.css', 'blackbox.css', 'fonts.css', 'favicon.svg']
for name in files + ['data', 'fonts']:
    if not (root / name).exists():
        raise FileNotFoundError(root / name)
if output.exists():
    shutil.rmtree(output)
output.mkdir()
for name in files:
    shutil.copy2(root / name, output / name)
for name in ['data', 'fonts']:
    shutil.copytree(root / name, output / name)
(output / '.nojekyll').touch()
print(f'Static site packaged in {output}')
