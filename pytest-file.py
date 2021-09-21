# Databricks notebook source
import pytest
import demo

# COMMAND ----------

def file_test():
  assert demo.func() == 3

file_test()

# COMMAND ----------
