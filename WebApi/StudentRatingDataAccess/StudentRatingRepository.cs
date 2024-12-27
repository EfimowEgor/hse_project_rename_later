using MySql.Data.MySqlClient;
using StudentRatingDomain.Entities;
using StudentRatingDomain.Repositories;

namespace StudentRatingDataAccess
{
    public sealed class StudentRatingRepository(string connectionString) : IStudentRatingRepository
    {
        private async Task<int> GetStudentIdByName(string firstName, string lastName, string patronymic)
        {
            var query = "SELECT Id FROM Students WHERE Name = @Name AND Surname = @Surname AND Patronymic = @Patronymic";

            using var connection = new MySqlConnection(connectionString);
            await connection.OpenAsync();

            using var command = new MySqlCommand(query, connection);
            command.Parameters.AddWithValue("@Name", firstName);
            command.Parameters.AddWithValue("@Surname", lastName);
            command.Parameters.AddWithValue("@Patronymic", patronymic);

            var id = await command.ExecuteScalarAsync();
            return Convert.ToInt32(id);
        }

        public async Task<IEnumerable<StudentRating>> GetCurrentStudentRatingsByNameAsync(string firstName, string lastName, string patronymic)
        {
            var studentId = await GetStudentIdByName(firstName, lastName, patronymic);
            var query = "SELECT StudentID, Program.Name, Course, Years, MODULES, Rating, MeanGrade, Percentile, GPA, MinGrade " +
                "FROM Stats " +
                "JOIN Program ON Stats.ProgramID = Program.id " +
                "JOIN Types ON Stats.TypeID = Types.id " +
                "WHERE StudentID = @StudentID AND TypeID = 1 " +
                "ORDER BY Years, MODULES";

            using var connection = new MySqlConnection(connectionString);
            await connection.OpenAsync();

            using var command = new MySqlCommand(query, connection);
            command.Parameters.AddWithValue("@StudentID", studentId);

            var ratings = new List<StudentRating>();
            using var reader = await command.ExecuteReaderAsync();

            while (await reader.ReadAsync())
            {
                var stundentId = reader.GetInt32(0);
                var programName = reader.GetString(1);
                var course = reader.GetInt32(2);
                var years = reader.GetString(3);
                var modules = reader.GetString(4);
                var place = reader.GetString(5);
                var meanGrade = reader.GetDouble(6);
                var percentile = reader.GetString(7);
                var gpa = reader.GetDouble(8);
                var minGrade = reader.GetDouble(9);

                ratings.Add(new(studentId, 1, programName, course, years, modules, place, meanGrade, minGrade, percentile, gpa));
            }

            return ratings;
        }

        public async Task<IEnumerable<StudentRating>> GetAfterRetakeStudentRatingsByNameAsync(string firstName, string lastName, string patronymic)
        {
            var studentId = await GetStudentIdByName(firstName, lastName, patronymic);
            var query = "SELECT StudentID, Program.Name, Course, Years, MODULES, Rating, MeanGrade, Percentile, GPA, MinGrade " +
                "FROM Stats " +
                "JOIN Program ON Stats.ProgramID = Program.id " +
                "JOIN Types ON Stats.TypeID = Types.id " +
                "WHERE StudentID = @StudentID AND TypeID = 4 " +
                "ORDER BY Years, MODULES";

            using var connection = new MySqlConnection(connectionString);
            await connection.OpenAsync();

            using var command = new MySqlCommand(query, connection);
            command.Parameters.AddWithValue("@StudentID", studentId);

            var ratings = new List<StudentRating>();
            using var reader = await command.ExecuteReaderAsync();

            while (await reader.ReadAsync())
            {
                var stundentId = reader.GetInt32(0);
                var programName = reader.GetString(1);
                var course = reader.GetInt32(2);
                var years = reader.GetString(3);
                var modules = reader.GetString(4);
                var place = reader.GetString(5);
                var meanGrade = reader.GetDouble(6);
                var percentile = reader.GetString(7);
                var gpa = reader.GetDouble(8);
                var minGrade = reader.GetDouble(9);

                ratings.Add(new(studentId, 4, programName, course, years, modules, place, meanGrade, minGrade, percentile, gpa));
            }

            return ratings;
        }

        public async Task<IEnumerable<StudentRating>> GetCumulativeStudentRatingsByNameAsync(string firstName, string lastName, string patronymic)
        {
            var studentId = await GetStudentIdByName(firstName, lastName, patronymic);
            var query = "SELECT StudentID, Program.Name, Course, Years, MODULES, Rating, MeanGrade, Percentile, GPA, MinGrade " +
                "FROM Stats " +
                "JOIN Program ON Stats.ProgramID = Program.id " +
                "JOIN Types ON Stats.TypeID = Types.id " +
                "WHERE StudentID = @StudentID AND TypeID = 2 " +
                "ORDER BY Years, MODULES";

            using var connection = new MySqlConnection(connectionString);
            await connection.OpenAsync();

            using var command = new MySqlCommand(query, connection);
            command.Parameters.AddWithValue("@StudentID", studentId);

            var ratings = new List<StudentRating>();
            using var reader = await command.ExecuteReaderAsync();

            while (await reader.ReadAsync())
            {
                var stundentId = reader.GetInt32(0);
                var programName = reader.GetString(1);
                var course = reader.GetInt32(2);
                var years = reader.GetString(3);
                var modules = reader.GetString(4);
                var place = reader.GetString(5);
                var meanGrade = reader.GetDouble(6);
                var percentile = reader.GetString(7);
                var gpa = reader.GetDouble(8);
                var minGrade = reader.GetDouble(9);

                ratings.Add(new(studentId, 2, programName, course, years, modules, place, meanGrade, minGrade, percentile, gpa));
            }

            return ratings;
        }

        public async Task<StudentRating> GetGraduateStudentRatingByNameAsync(string firstName, string lastName, string patronymic)
        {
            var studentId = await GetStudentIdByName(firstName, lastName, patronymic);
            var query = "SELECT StudentID, Program.Name, Course, Years, MODULES, Rating, MeanGrade, Percentile, GPA, MinGrade " +
                "FROM Stats " +
                "JOIN Program ON Stats.ProgramID = Program.id " +
                "JOIN Types ON Stats.TypeID = Types.id " +
                "WHERE StudentID = @StudentID AND TypeID = 3 " +
                "ORDER BY Years, MODULES";

            using var connection = new MySqlConnection(connectionString);
            await connection.OpenAsync();

            using var command = new MySqlCommand(query, connection);
            command.Parameters.AddWithValue("@StudentID", studentId);

            using var reader = await command.ExecuteReaderAsync();
            await reader.ReadAsync();

            var stundentId = reader.GetInt32(0);
            var programName = reader.GetString(1);
            var course = reader.GetInt32(2);
            var years = reader.GetString(3);
            var modules = reader.GetString(4);
            var place = reader.GetString(5);
            var meanGrade = reader.GetDouble(6);
            var percentile = reader.GetString(7);
            var gpa = reader.GetDouble(8);
            var minGrade = reader.GetDouble(9);

            var rating = new StudentRating(studentId, 3, programName, course, years, modules, place, meanGrade, minGrade, percentile, gpa);
            return rating;
        }
    }
}
