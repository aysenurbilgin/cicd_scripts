test_input_data = {'State': {'0': 'KS'},
 'Account_Length': {'0': 128},
 'Area_Code': {'0': 415},
 'Phone': {'0': '382-4657'},
 'Intl_Plan': {'0': 'no'},
 'VMail_Plan': {'0': 'yes'},
 'VMail_Message': {'0': 25},
 'Day_Mins': {'0': 265.1},
 'Day_Calls': {'0': 110},
 'Day_Charge': {'0': 45.07},
 'Eve_Mins': {'0': 197.4},
 'Eve_Calls': {'0': 99},
 'Eve_Charge': {'0': 16.78},
 'Night_Mins': {'0': 244.7},
 'Night_Calls': {'0': 91},
 'Night_Charge': {'0': 11.01},
 'Intl_Mins': {'0': 10.0},
 'total_Mins': {'0': 717.2},
 'Intl_Calls': {'0': 3},
 'Intl_Charge': {'0': 2.7},
 'Total_Charge': {'0': 75.56},
 'CustServ_Calls': {'0': 1},
 'Churn': {'0': 1}}


test_output_data ={
        "State":{"0":"KS"},
        "revenue_loss":{"0":75.56},
        "loss_type":{"0":"Current"}}