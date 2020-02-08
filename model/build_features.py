import pandas as pd

math_student_df = pd.read_csv('../data/raw/student-mat.csv')
math_student_por = pd.read_csv('../data/raw/student-por.csv')


def convert_to_binary(arg1, arg2, df_series, df):
    df[df_series] = df[df_series].map({arg1: 1, arg2: 0})
    return df


def clean_columns(df):
    df.drop(['school', 'address', 'Mjob', 'Fjob', 'reason',
             'guardian', 'paid', 'nursery', 'schoolsup', 'higher',
             'activities', 'Walc'], inplace=True, axis=1)
    modify_columns = ['famsup', 'internet', 'romantic',]

    for x in modify_columns:
        df = convert_to_binary('yes', 'no', x, df)

    df = convert_to_binary('F', 'M', 'sex', df)
    df = convert_to_binary('LE3', 'GT3', 'famsize', df)
    df = convert_to_binary('T', 'A', 'Pstatus', df)
    df.to_csv('../data/processed/cleaned_data.csv',index=False)


# if __name__ == "main":
clean_columns(math_student_df)