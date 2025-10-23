from configs.configs import configuure_arguument_parser
from utils.average_ratings import average_raiting
from utils.load_csv import read_csv_files
from utils.outputs import pretty_output


MODE_TO_FUNCTION = {'pretty_output': pretty_output}


def main():
    parser = configuure_arguument_parser(MODE_TO_FUNCTION.keys())
    args = parser.parse_args()
    data = read_csv_files(args.files)
    report = MODE_TO_FUNCTION.get(args.report)
    if not report:
        print(f'Неизвестный отчет: {args.report}')
        return
    report_data = average_raiting(data)
    pretty_output(report_data)


if __name__ == '__main__':
    main()
