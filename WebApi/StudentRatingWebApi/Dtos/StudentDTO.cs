namespace StudentRatingWebApi.Dtos
{
    public sealed class StudentDto
    {
        public required string LastName { get; init; }

        public required string FirstName { get; init; }

        public required string Patronymic { get; init; }
    }
}
