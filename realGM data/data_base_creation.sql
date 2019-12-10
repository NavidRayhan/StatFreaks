CREATE TABLE International_Transactions(
    ID INTEGER PRIMARY KEY,
    Player VARCHAR(50) NOT NULL,
    Date VARCHAR(50) NOT NULL, /* sqlite3 has no date-time datatype */
    Action TEXT NOT NULL,
    Previous_team VARCHAR(50),
    New_team VARCHAR(50)
)