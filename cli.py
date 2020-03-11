import argparse
import pkgutil
import scripts

# Start by creating our top-level parser, serving as the entrypoint to
# all commands in `scripts`
parser = argparse.ArgumentParser()
subparser = parser.add_subparsers()


# Automatically create a command named after each submodule in our
# `scripts` module
for importer, modname, ispkg in pkgutil.iter_modules(scripts.__path__):
    mod_parser = subparser.add_parser(modname)

    # Dispatch to the submodule to have it create its subcommand
    # parser
    getattr(scripts, modname).create_parser(mod_parser)


# Execute our wrapper script
if __name__ == "__main__":
    args = parser.parse_args()

    # Each subcommand sets args.dispatch to the command it wants to
    # execute, accepting `args` as the only argument
    args.dispatch(args)
