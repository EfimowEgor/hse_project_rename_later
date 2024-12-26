using AutoMapper;
using StudentRatingDomain.Entities;
using StudentRatingWebApi.Dtos;

namespace StudentRatingWebApi.Profiles
{
    public class StudentProfile : Profile
    {
        public StudentProfile()
        {
            CreateMap<Student, StudentDto>();
        }
    }
}
