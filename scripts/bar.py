def bar(args):
    print(f"test2={args.test2}")


def create_parser(parser):
    parser.add_argument("test2")
    parser.set_defaults(dispatch=bar)
    return parser
