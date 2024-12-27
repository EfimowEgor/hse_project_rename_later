using AutoMapper;
using StudentRatingDomain.Entities;
using StudentRatingWebApi.Dtos;

namespace StudentRatingWebApi.Profiles
{
    internal sealed class StudentRatingProfile : Profile
    {
        public StudentRatingProfile()
        {
            CreateMap<StudentRating, StudentRatingDto>();
        }
    }
}
