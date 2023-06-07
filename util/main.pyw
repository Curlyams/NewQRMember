import os
import numpy as np
import pandas as pd
import openpyxl as op
import qr_functions

def main(export_path,master_path,clinic_address):


    # Load in member export
    #export_path = input("Enter the file path of the export file")
    try:
        export_df = qr_functions.load_export_df(export_path)
        # Open Master QR Export file
        #master_qr_path = input("Enter Master QR path.")
        all_member_ws,member_wb = qr_functions.load_master_qr_sheet(master_path)

        

        #Isolate members with QR codes
        #member_id_lst = qr_functions.members_with_codes(all_member_ws)

        #Retrieve all members from export who go to participating clinics

        member_at_participating_clinics = qr_functions.all_members_at_clinics(export_df,clinic_address)

        #Isolate new members who are not on the qr master sheet

        new_members = qr_functions.new_member_finder(all_member_ws,member_at_participating_clinics)
        #Add new members to excel sheet.
        if new_members.empty:
            return "No New Members"

        else:
            qr_functions.add_members_data_to_sheet(new_members,all_member_ws)
            #save changes of excel sheet.
            member_wb.save(master_path)

    except Exception as e:
        #Displays an error message if exception is raised
        return str(e)

if __name__ == "__main__":
    main()










