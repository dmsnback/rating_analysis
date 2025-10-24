from configs.configs import configuure_arguument_parser
from errors.exceptions import UnknownReportException
from reports.average_ratings import average_rating
from utils.load_csv import read_csv_files
from utils.outputs import pretty_output


REPORTS = {'average-rating': average_rating}


def main():
    parser = configuure_arguument_parser(REPORTS.keys())
    args = parser.parse_args()
    data = read_csv_files(args.files)
    report = REPORTS.get(args.report)
    if not report:
        raise UnknownReportException(f'Неизвестный отчет: {args.report}')
    report_data = report(data)
    pretty_output(report_data)


if __name__ == '__main__':
    main()
