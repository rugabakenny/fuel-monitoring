users must have all be in relation with their functions
for login
    * we need to send username and password in json format
    return
        all user info except password in json format

            AccountID/USERID
            FirstName
            LastName.
            phoneNo
            email
            UserType
            Username
            AccountStatus
            session key
getting company
 request should include session key in order to know who is requesting data and what to return
######################################################################################
#######################################################################################
user types
   { system admin
       funct
         adding companies
         adding meters
         creating companies admin
         disactivating/activating user
         adding payment plan
         adding system technician
         
    } == ???????
######################################################################################
#######################################################################################
   { company admin
        adding company staff/techninician
        adding company station
        adding company station managers
        adding company station dispenser and rotation
   }== ???????
######################################################################################
#######################################################################################      
      {
       company staff
          view only all info about company and export
       }== ???????
######################################################################################
#######################################################################################         
     {
        company techinician
           adding/ editing station configuration
                     station tank(s)
                     station island(s)
                     station pump(s)
                     station nozzles
          view station configuration of the company
     } == ???????
######################################################################################
#######################################################################################
     {
       station manager
          recording shift tank data(dumping data)
          view station consumption

     }== ???????

#######################################################################################
#######################################################################################
 {
    station dispenser
        adding /pump/nozzle index numbers (start and end shift number).
        view history of index numbers of station (s)he works from.
}== ???????