# We call this function to do anything related to the `foo` subcommand
def foo(args):
    print(f"test1={args.test1}")
    print(f"--global-arg: {args.global_arg}")


# Define our subparser for `foo`
def create_parser(parser):
    parser.add_argument("test1")
    parser.set_defaults(dispatch=foo)
    return parser
