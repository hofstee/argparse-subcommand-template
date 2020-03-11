# We call this function to do anything related to the `bar` subcommand
def bar(args):
    print(f"test2={args.test2}")


# Define our subparser for `foo`
def create_parser(parser):
    parser.add_argument("test2")
    parser.set_defaults(dispatch=bar)
    return parser
