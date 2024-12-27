namespace StudentRatingWebApi.Dtos
{
    public sealed class StudentRatingDto
    {
        public required string ProgramName { get; init; }

        public required int Course { get; init; }

        public required string Years { get; init; }

        public required string Modules { get; init; }

        public required string Place { get; init; }

        public required double MeanGrade { get; init; }

        public required double MinGrade { get; init; }

        public required string Percentile { get; init; }

        public required double Gpa { get; init; }
    }
}
