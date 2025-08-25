from src.states.blogstate import BlogState
from langchain_core.messages import SystemMessage,HumanMessage
from src.states.blogstate import Blog
class BlogNode:
    """
    A class to represent the blog node
    """
    def __init__(self,llm):
        self.llm=llm

    def title_creation(self,state:BlogState):
        """
        create the title for the blog 
        """
        if "topic" in state and state["topic"]:
            prompt="""
                You are an expert content writer. Use Markdown formatting. Generate 
                a blog title for the {topic}. This title should be created and SEO friendly
                """
            
            system_message=prompt.format(topic=state["topic"])
            response=self.llm.invoke(system_message)
            return {"blog":{"title":response.content}}
    
    def content_generation(self,state:BlogState):
        if "topic" in state and state["topic"]:
            system_prompt="""You are an expert blog writer. Use Markdown formatting.
            Generate a detailed blog content with detailed breakdown for the topic {topic}"""
            system_message=system_prompt.format(topic=state["topic"])
            response=self.llm.invoke(system_message)
            return {"blog":{"title":state['blog']['title'],"content":response.content}}
        
    # def translation(self,state:BlogState):
    #     """
    #     Translate the content to the specified language
    #     """
    #     translation_prompt="""
    #     Translate the following content into {current_language}.
    #     -Maintain the original tone, style, and formatting.
    #     - Adapt cultural references and idioms to be appropriate for {current_language}.

    #     ORGINAL CONTENT:
    #     {blog_content}
    #     """

    #     blog_content=state["blog"]["content"]
    #     message=[
    #         HumanMessage(translation_prompt.format(current_language=state["current_language"],blog_content=blog_content))
    #     ]
    #     translation_content=self.llm.with_structed_output(Blog).invoke(message)

    def translation(self, state: BlogState):
        """
        Translate the content to the specified language
        """
        translation_prompt = f"""
        Translate the following content into {state["current_language"]}.
        - Maintain the original tone, style, and formatting.
        - Adapt cultural references and idioms to be appropriate for {state["current_language"]}.

        ORIGINAL CONTENT:
        {state["blog"]["content"]}
        """

        # Build message
        message = [HumanMessage(content=translation_prompt)]

        # Call LLM with structured output into Blog schema
        translation_content: Blog = self.llm.with_structured_output(Blog).invoke(message)

        # ✅ Return updated state with translated blog
        return {
            "blog": {
                "title": translation_content.title,
                "content": translation_content.content
            }
        }


    
    def route(self,state:BlogState):
        return {"current_language":state['current_language']}
    

    def route_decision(self,state:BlogState):
        if state["current_language"]=="marathi":
            return "marathi"
        elif state["current_language"]=="french":
            return "french"
        else:
            return state["current_language"]

