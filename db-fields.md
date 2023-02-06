# Database Fields

## Ride
- rid: int
- driver_id: int 
- owner_id: int
- owner_party_size: int
- sharers: [{sharer_id: int, sharer_party_size: int}, ...]
- required_arrival_time: datetime
- pickup_location: string
- destination: string
- (destination_lat: float)
- status: string(open, confirmed, canceled, completed)
- allow_sharing: bool
- special_requirements: string
- (pickup_lat: float)
- (pickup_long: float)
- (destination_long: float)
- (destination_lat: float)
- (pickup_time: datetime)



## Account
- uid: int
- first_name: string
- last_name: string
- email: string
- phone: string
- password: string
- (profile_picture: string)
- is_driver: bool
- (vehical color: string)
- (vehical plate: string)
- (vehical make: string)
- (vehical model: string)
- (vehical year: int)
- (vehical seats: int)
- (driving license: string)
- (driving license expiration: datetime)
- (driving license state: string)
