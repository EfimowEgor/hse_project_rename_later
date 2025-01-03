﻿using AutoMapper;
using StudentRatingDomain.Entities;
using StudentRatingWebApi.Dtos;

namespace StudentRatingWebApi.Profiles
{
    internal sealed class StudentProfile : Profile
    {
        public StudentProfile()
        {
            CreateMap<Student, StudentDto>();
        }
    }
}
