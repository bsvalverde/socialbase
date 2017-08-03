Feature: guarantee platform integration

  Scenario Outline: blog and twitter integration
     Given the post <title> is on the blog
      then there should be a tweet about it

   Examples:
   | title |
   | A importância de segmentar a Comunicação Interna |