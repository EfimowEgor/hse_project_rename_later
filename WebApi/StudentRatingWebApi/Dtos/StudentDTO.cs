using System.ComponentModel;
using System.ComponentModel.DataAnnotations;

namespace StudentRatingWebApi.Dtos
{
    public sealed class StudentDto
    {
        [Required]
        [Description("Фамилия студента")]
        public required string LastName { get; init; }

        [Required]
        [Description("Имя студента")]
        public required string FirstName { get; init; }

        [Required]
        [Description("Отчество студента")]
        public required string Patronymic { get; init; }
    }
}
