def inspect_data(df):
    print("\n" + "=" * 50)
    print("DATASET INFORMATION")
    print("=" * 50)

    print("\nShape:")
    print(df.shape)

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())


def show_missing_rows(df):
    print("\nRows with missing Postal Code:")

    print(
        df[df["Postal Code"].isnull()][
            [
                "Order ID",
                "Customer Name",
                "City",
                "State",
                "Postal Code",
                "Region",
                "Sales",
                "Profit",
            ]
        ]
    )
def clean_data(df):

    return df

def feature_engineering(df):
    # Shipping Days
    df["Shipping Days"] = (
        df["Ship Date"] - df["Order Date"]
    ).dt.days

    # Profit Margin (%)
    df["Profit Margin"] = (
        df["Profit"] / df["Sales"]
    ) * 100

    # Order Month
    df["Order Month"] = df["Order Date"].dt.month_name()

    # Order Year
    df["Order Year"] = df["Order Date"].dt.year

    # Quarter
    df["Quarter"] = df["Order Date"].dt.quarter

    # Weekday
    df["Weekday"] = df["Order Date"].dt.day_name()

    return df