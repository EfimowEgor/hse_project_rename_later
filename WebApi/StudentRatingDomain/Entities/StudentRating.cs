namespace StudentRatingDomain.Entities
{
    public sealed record StudentRating(int StudentId,
        int RatingId,
        string ProgramName,
        int Course,
        string Years,
        string Modules,
        string Place,
        double MeanGrade,
        double MinGrade,
        string Percentile,
        double Gpa)
    {

    }
}
