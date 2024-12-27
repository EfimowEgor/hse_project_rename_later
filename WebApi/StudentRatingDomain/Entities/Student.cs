namespace StudentRatingDomain.Entities
{
    public sealed record Student(int Id,
        string FirstName, 
        string LastName, 
        string Patronymic)
    {

    }
}
