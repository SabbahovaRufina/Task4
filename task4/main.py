import asyncio
from read_csv import get_df_from_csv, write_to_excel
import pandas
import matplotlib.pyplot as plt


async def subtask1(df):
    df_res = (df.groupby(df['Дата документа'].dt.month).agg({'Идентификатор документа': ['count']}))
    return df_res


async def subtask2(df1, df2):
    df_res = df1.set_index('Идентификатор филиалы документа').join(df2.set_index('Идентификатор филиала'))
    df_res['Неделя'] = df_res['Дата документа'].dt.isocalendar().week
    res = pandas.crosstab(df_res['Неделя'],
                          df_res['Наименование региона филиала'],
                          values=df_res['Идентификатор документа'],
                          aggfunc='count',
                          normalize=False)
    res.plot()
    plt.show()
    return res


async def main():
    df_data = await get_df_from_csv(r"data\data.csv")
    df_data['Дата документа'] = pandas.to_datetime(df_data['Дата документа'])
    df_catalog = await get_df_from_csv(r"data\Справочник.csv")
    df1, df2 = await subtask1(df_data), await subtask2(df_data, df_catalog)
    await write_to_excel(Лист1=df1, Лист2=df2)


if __name__ == '__main__':
    try:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(main())
    except KeyboardInterrupt:
        exit(0)


