import pandas
import asyncio


async def get_df_from_csv(path):
    return pandas.read_csv(path, sep=',', encoding='utf-8')


async def write_to_excel(result_file="result_data.xlsx", **df_sheet):
    try:
        writer = pandas.ExcelWriter(result_file, engine='xlsxwriter')
        for sheet, df in df_sheet.items():
            df.to_excel(writer, sheet, index=True)
        writer.close()
    except PermissionError:
        print("закройте эксель файл")
        exit(0)


async def print_df_from_csv(path):
    df = await get_df_from_csv(path)
    print(df.columns.values.tolist())


async def main():
    await print_df_from_csv(r"data\Справочник.csv")
    await print_df_from_csv(r"data\data.csv")


if __name__ == '__main__':
    try:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(main())
    except KeyboardInterrupt:
        exit(0)
