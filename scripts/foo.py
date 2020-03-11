def foo(args):
    print(f"test1={args.test1}")


def create_parser(parser):
    parser.add_argument("test1")
    parser.set_defaults(dispatch=foo)
    return parser
