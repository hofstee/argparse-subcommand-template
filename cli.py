import argparse
import pkgutil
import scripts

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest='command')

for importer, modname, ispkg in pkgutil.iter_modules(scripts.__path__):
    mod_parser = subparser.add_parser(modname)
    getattr(getattr(scripts, modname), 'create_parser')(mod_parser)

if __name__ == "__main__":
    args = parser.parse_args()
    args.dispatch(args)
